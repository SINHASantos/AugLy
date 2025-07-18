#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

# pyre-unsafe

from augly.text.composition import Compose, OneOf
from augly.text.functional import (
    apply_lambda,
    change_case,
    contractions,
    encode_text,
    get_baseline,
    insert_punctuation_chars,
    insert_text,
    insert_whitespace_chars,
    insert_zero_width_chars,
    merge_words,
    replace_bidirectional,
    replace_fun_fonts,
    replace_similar_chars,
    replace_similar_unicode_chars,
    replace_text,
    replace_upside_down,
    replace_words,
    simulate_typos,
    split_words,
    swap_gendered_words,
)
from augly.text.intensity import (
    apply_lambda_intensity,
    base64_intensity,
    change_case_intensity,
    contractions_intensity,
    encode_text_intensity,
    get_baseline_intensity,
    insert_punctuation_chars_intensity,
    insert_text_intensity,
    insert_whitespace_chars_intensity,
    insert_zero_width_chars_intensity,
    merge_words_intensity,
    replace_bidirectional_intensity,
    replace_fun_fonts_intensity,
    replace_similar_chars_intensity,
    replace_similar_unicode_chars_intensity,
    replace_text_intensity,
    replace_upside_down_intensity,
    replace_words_intensity,
    simulate_typos_intensity,
    split_words_intensity,
    swap_gendered_words_intensity,
)
from augly.text.transforms import (
    ApplyLambda,
    ChangeCase,
    Contractions,
    EncodeTextTransform,
    GetBaseline,
    InsertPunctuationChars,
    InsertText,
    InsertWhitespaceChars,
    InsertZeroWidthChars,
    MergeWords,
    ReplaceBidirectional,
    ReplaceFunFonts,
    ReplaceSimilarChars,
    ReplaceSimilarUnicodeChars,
    ReplaceText,
    ReplaceUpsideDown,
    ReplaceWords,
    SimulateTypos,
    SplitWords,
    SwapGenderedWords,
)

__all__ = [
    "Compose",
    "OneOf",
    "ApplyLambda",
    "ChangeCase",
    "Contractions",
    "EncodeTextTransform",
    "GetBaseline",
    "InsertPunctuationChars",
    "InsertText",
    "InsertWhitespaceChars",
    "InsertZeroWidthChars",
    "MergeWords",
    "ReplaceBidirectional",
    "ReplaceFunFonts",
    "ReplaceSimilarChars",
    "ReplaceSimilarUnicodeChars",
    "ReplaceText",
    "ReplaceUpsideDown",
    "ReplaceWords",
    "SimulateTypos",
    "SplitWords",
    "SwapGenderedWords",
    "apply_lambda",
    "change_case",
    "contractions",
    "encode_text",
    "get_baseline",
    "insert_punctuation_chars",
    "insert_text",
    "insert_whitespace_chars",
    "insert_zero_width_chars",
    "merge_words",
    "replace_bidirectional",
    "replace_fun_fonts",
    "replace_similar_chars",
    "replace_similar_unicode_chars",
    "replace_text",
    "replace_upside_down",
    "replace_words",
    "simulate_typos",
    "split_words",
    "swap_gendered_words",
    "apply_lambda_intensity",
    "base64_intensity",
    "change_case_intensity",
    "contractions_intensity",
    "encode_text_intensity",
    "get_baseline_intensity",
    "insert_punctuation_chars_intensity",
    "insert_text_intensity",
    "insert_whitespace_chars_intensity",
    "insert_zero_width_chars_intensity",
    "merge_words_intensity",
    "replace_bidirectional_intensity",
    "replace_fun_fonts_intensity",
    "replace_similar_chars_intensity",
    "replace_similar_unicode_chars_intensity",
    "replace_text_intensity",
    "replace_upside_down_intensity",
    "replace_words_intensity",
    "simulate_typos_intensity",
    "split_words_intensity",
    "swap_gendered_words_intensity",
]
