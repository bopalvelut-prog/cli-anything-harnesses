import click
@click.group()
def cli(): pass
@cli.command()
def train(): click.echo('Unsloth train')
@cli.command()
def fast(): click.echo('Unsloth fast')
if __name__ == '__main__': cli()
