
help: Makefile
	@echo
	@echo " Choose a command run in Vanguard:"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo


.PHONY: help
