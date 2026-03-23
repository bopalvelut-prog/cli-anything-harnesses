import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autoscaler running')
@cli.command()
def start(): click.echo('autoscaler started')
if __name__ == '__main__': cli()
