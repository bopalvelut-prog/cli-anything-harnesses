import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('descheduler running')
@cli.command()
def start(): click.echo('descheduler started')
if __name__ == '__main__': cli()
