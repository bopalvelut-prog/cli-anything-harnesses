import click
@click.group()
def cli(): pass
@cli.command()
def train(): click.echo('Tokenizers train')
@cli.command()
def encode(): click.echo('Tokenizers encode')
if __name__ == '__main__': cli()
