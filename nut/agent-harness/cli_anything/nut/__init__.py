import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nut running')
@cli.command()
def start(): click.echo('nut started')
if __name__ == '__main__': cli()
