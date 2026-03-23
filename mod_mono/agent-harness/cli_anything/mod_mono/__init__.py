import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mod_mono running')
@cli.command()
def start(): click.echo('mod_mono started')
if __name__ == '__main__': cli()
