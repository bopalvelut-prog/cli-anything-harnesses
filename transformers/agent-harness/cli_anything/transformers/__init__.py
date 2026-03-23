import click
@click.group()
def cli(): pass
@cli.command()
def run(): click.echo('Transformers run')
@cli.command()
def models(): click.echo('Transformers models')
if __name__ == '__main__': cli()
