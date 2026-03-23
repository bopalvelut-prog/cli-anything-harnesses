import click
@click.group()
def cli(): pass
@cli.command()
def launch(): click.echo('Accelerate launch')
@cli.command()
def config(): click.echo('Accelerate config')
if __name__ == '__main__': cli()
