#!/usr/bin/make

all: $(patsubst %.Rmd,%.html,$(wildcard *.Rmd)) 

%.html: %.Rmd
	Rscript -e 'library(rmarkdown); rmarkdown::render("$<", output_file = "$@")'

new: all
	firefox *.html

homepage: all
	cp *.html ~/Projects/homepage/teaching/2020-summer/intro_to_programming/

clean:
	rm *.html
	rm -r *_files
	rm -r *_cache

.PHONY: clean all
