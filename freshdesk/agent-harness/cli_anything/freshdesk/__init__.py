import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def tickets(): click.echo('Freshdesk tickets')
@cli.command()
def agents(): click.echo('Freshdesk agents')
if __name__ == '__main__': cli()
