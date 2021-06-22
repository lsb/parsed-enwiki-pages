#!/bin/bash
# which jq || (sudo apt update && apt install -y jq)
# which parallel || (sudo apt update && apt install -y parallel) # we use a new-ish --delay 10sauto construction, as below
# which xq || (pip3 install yq)
wget -r -nd -l 1 -nc --accept-regex=".*pages-articles-multistream.*xml-.*bz2" https://dumps.wikimedia.your.org/enwiki/$(date +%Y%m01)/
ls -S *pages-articles-multistream*bz2 | parallel --memfree 20G --delay 60sauto --progress --retries 20 "bzcat {} | xq -c '.mediawiki.page[] | select(.ns== \"0\") | [.id, .title, .revision.text[\"#text\"]]' | sort | python3 id-title-text_to_id-title-body-entropy.py" | tee >(split -C 250000000 -x - id-title-body-entropy.json.) | python3 id-title-body-entropy_to_sqlite3.py
