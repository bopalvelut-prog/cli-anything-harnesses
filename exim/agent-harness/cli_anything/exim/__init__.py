import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Exim running')
@cli.command()
def queue(): click.echo('Exim queue')
if __name__ == '__main__': cli()
