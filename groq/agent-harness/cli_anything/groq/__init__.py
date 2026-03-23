import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('Groq chat')
@cli.command()
def models(): click.echo('Groq models')
if __name__ == '__main__': cli()
