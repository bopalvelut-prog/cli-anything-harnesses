import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('Mistral chat')
@cli.command()
def models(): click.echo('Mistral models')
if __name__ == '__main__': cli()
