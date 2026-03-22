import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Timular tracking started')
@cli.command()
def stop(): click.echo('Timular tracking stopped')
if __name__ == '__main__': cli()
