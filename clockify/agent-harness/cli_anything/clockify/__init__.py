import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Clockify timer started')
@cli.command()
def stop(): click.echo('Clockify timer stopped')
if __name__ == '__main__': cli()
