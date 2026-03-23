import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('Aider chat')
@cli.command()
def models(): click.echo('Aider models')
if __name__ == '__main__': cli()
