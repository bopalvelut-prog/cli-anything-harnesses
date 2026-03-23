import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('throat running')
@cli.command()
def start(): click.echo('throat started')
if __name__ == '__main__': cli()
