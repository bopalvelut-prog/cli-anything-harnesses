import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('RescueTime running')
@cli.command()
def report(): click.echo('RescueTime report')
if __name__ == '__main__': cli()
