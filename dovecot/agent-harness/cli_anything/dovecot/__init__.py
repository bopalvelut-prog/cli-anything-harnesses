import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Dovecot running')
@cli.command()
def users(): click.echo('Dovecot users')
if __name__ == '__main__': cli()
