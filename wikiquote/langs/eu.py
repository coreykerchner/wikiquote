from typing import List, Text, Tuple

import lxml

from .. import utils

WORD_BLACKLIST = ["Iturria:", "Jatorrizkoan ", "Testuingurua:"]
MAIN_PAGE = "Azala"
HEADINGS = ["kanpo loturak", "erreferentziak"]


def extract_quotes(tree: lxml.html.HtmlElement, max_quotes: int) -> List[Text]:
    q_lst = utils.extract_quotes_li(tree, max_quotes, HEADINGS, WORD_BLACKLIST)
    return [utils.remove_credit(q) for q in q_lst]


def qotd(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    tree = html_tree.get_element_by_id("mf-qotd")

    selector = "div/div/table/tbody/tr"
    raw_quote = tree.xpath(selector)[0].text_content().split("~")
    quote = raw_quote[0].strip()
    author = raw_quote[1].strip()

    return quote, author
