import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def contacts(): click.echo('Brevo contacts')
@cli.command()
def campaigns(): click.echo('Brevo campaigns')
if __name__ == '__main__': cli()
