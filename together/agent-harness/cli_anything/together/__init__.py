import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('Together AI chat')
@cli.command()
def models(): click.echo('Together AI models')
if __name__ == '__main__': cli()
