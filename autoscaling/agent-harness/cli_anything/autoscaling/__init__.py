import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autoscaling running')
@cli.command()
def start(): click.echo('autoscaling started')
if __name__ == '__main__': cli()
