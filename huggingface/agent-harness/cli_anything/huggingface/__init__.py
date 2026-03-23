import click
@click.group()
def cli(): pass
@cli.command()
def login(): click.echo('HuggingFace login')
@cli.command()
def models(): click.echo('HuggingFace models')
if __name__ == '__main__': cli()
