import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('watchdog running')
@cli.command()
def start(): click.echo('watchdog started')
if __name__ == '__main__': cli()
