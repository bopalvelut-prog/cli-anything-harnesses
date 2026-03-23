import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apache_struts running')
@cli.command()
def start(): click.echo('apache_struts started')
if __name__ == '__main__': cli()
