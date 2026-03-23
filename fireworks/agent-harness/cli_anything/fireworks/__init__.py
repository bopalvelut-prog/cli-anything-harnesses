import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('Fireworks AI chat')
@cli.command()
def models(): click.echo('Fireworks AI models')
if __name__ == '__main__': cli()
