import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Toggl timer started')
@cli.command()
def stop(): click.echo('Toggl timer stopped')
if __name__ == '__main__': cli()
