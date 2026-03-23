import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('manifest running')
@cli.command()
def start(): click.echo('manifest started')
if __name__ == '__main__': cli()
