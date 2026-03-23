import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('owasp running')
@cli.command()
def start(): click.echo('owasp started')
if __name__ == '__main__': cli()
