import click
@click.group()
def cli(): pass
@cli.command()
def suggest(): click.echo('Copilot suggest')
@cli.command()
def chat(): click.echo('Copilot chat')
if __name__ == '__main__': cli()
