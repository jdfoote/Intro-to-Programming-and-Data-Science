#!/usr/bin/make

all: $(patsubst %.Rmd,%.html,$(wildcard *.Rmd)) 

%.html: %.Rmd
	Rscript -e 'library(rmarkdown); rmarkdown::render("$<", output_file = "$@")'

new: all
	firefox *.html

clean:
	rm *.html
	rm -r *_files
	rm -r *_cache

.PHONY: clean all
