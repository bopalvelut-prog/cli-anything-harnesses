import click
@click.group()
def cli(): pass
@cli.command()
def run(): click.echo('Replicate run')
@cli.command()
def models(): click.echo('Replicate models')
if __name__ == '__main__': cli()
