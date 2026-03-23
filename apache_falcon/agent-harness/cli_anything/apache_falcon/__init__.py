import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apache_falcon running')
@cli.command()
def start(): click.echo('apache_falcon started')
if __name__ == '__main__': cli()
