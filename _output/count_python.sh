#!/bin/bash
data_dir="."
grep -i "python" "$data_dir/questions.csv" "$data_dir/question_tags.csv" | wc -l
