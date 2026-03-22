import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Tally forms')
@cli.command()
def responses(): click.echo('Tally responses')
if __name__ == '__main__': cli()
