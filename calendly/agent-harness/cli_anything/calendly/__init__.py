import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def events(): click.echo('Calendly events')
if __name__ == '__main__': cli()
