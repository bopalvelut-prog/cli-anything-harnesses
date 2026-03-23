import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mlx running')
@cli.command()
def start(): click.echo('mlx started')
if __name__ == '__main__': cli()
