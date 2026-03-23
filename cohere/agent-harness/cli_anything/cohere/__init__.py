import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('Cohere chat')
@cli.command()
def embed(): click.echo('Cohere embed')
if __name__ == '__main__': cli()
