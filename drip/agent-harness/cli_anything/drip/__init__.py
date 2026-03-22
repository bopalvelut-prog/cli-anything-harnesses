import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def subscribers(): click.echo('Drip subscribers')
@cli.command()
def campaigns(): click.echo('Drip campaigns')
if __name__ == '__main__': cli()
