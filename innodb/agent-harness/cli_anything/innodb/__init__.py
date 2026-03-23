import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('innodb running')
@cli.command()
def start(): click.echo('innodb started')
if __name__ == '__main__': cli()
