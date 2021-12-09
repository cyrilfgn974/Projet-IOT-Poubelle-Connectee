doc:
	mkdir doc
	pandoc Architecture.md -o doc/Architecture.pdf
	pandoc Description_rendu_partiel.md -o doc/Description_rendu_partiel.pdf

clean:
	rm -rf doc/