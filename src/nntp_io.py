#!/usr/bin/env python3

import json
import nntplib  # Removed from the Standard Library in Python 3.13.

# import pathlib
import uuid

FMT = """\
From: GitHub Actions <actions@github.com>
Newsgroups: {}
Subject: inews test
Message-ID: <test.inews.{}@inn2.packages.debian.org>

{}
"""


def nntp_write(payload: dict, newsgroup: str = "local.test") -> str:
    """
    Write a payload dict as json to a InterNet News newsgroup.

    Return: test.inews.a253222105b64597b9afd10e4f4c6740@inn2.packages.debian.org
    """
    msg = FMT.format(newsgroup, uuid.uuid4().hex, json.dumps(payload, indent=2))
    # print(f"{msg = }")
    with nntplib.NNTP("localhost", readermode=True) as nntp_server:
        response = nntp_server.post(msg.encode("utf-8")).split()
        assert response[0] == "240", " ".join(response)
        return response[-1]


def nntp_read(article_id: str, newsgroup: str = "local.test") -> dict:
    """
    Read an article from a InterNet News newsgroup and return it as a dict.
    """
    with nntplib.NNTP("localhost", readermode=True) as nntp_server:
        resp, count, first, last, name = nntp_server.group(newsgroup)
        assert last, f"{newsgroup = } has no articles."
        article = nntp_server.article(article_id)
        body_lines = article[1].lines[10:]  # Skip the header lines.
        assert body_lines, f"{article_id = }: {article = } has no body."
        body = "\n".join(line.decode("utf-8") for line in body_lines)
        # print(f"{body = }")
        return json.loads(body)


if __name__ == "__main__":
    payload = {"key": "value"}
    article_id = nntp_write(payload)
    print(f"{article_id = }")
    print(nntp_read(article_id))
