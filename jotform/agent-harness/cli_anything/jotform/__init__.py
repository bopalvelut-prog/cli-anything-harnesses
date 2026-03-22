import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('JotForm forms')
@cli.command()
def submissions(): click.echo('JotForm submissions')
if __name__ == '__main__': cli()
