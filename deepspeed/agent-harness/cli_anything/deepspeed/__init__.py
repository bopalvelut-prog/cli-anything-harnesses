import click
@click.group()
def cli(): pass
@cli.command()
def train(): click.echo('DeepSpeed train')
@cli.command()
def config(): click.echo('DeepSpeed config')
if __name__ == '__main__': cli()
