import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('tawk.to started')
if __name__ == '__main__': cli()
