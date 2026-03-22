import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Hubstaff timer started')
@cli.command()
def stop(): click.echo('Hubstaff timer stopped')
if __name__ == '__main__': cli()
