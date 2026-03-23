import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apache_jmeter running')
@cli.command()
def start(): click.echo('apache_jmeter started')
if __name__ == '__main__': cli()
