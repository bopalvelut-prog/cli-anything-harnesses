import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pidgin running')
@cli.command()
def start(): click.echo('pidgin started')
if __name__ == '__main__': cli()
