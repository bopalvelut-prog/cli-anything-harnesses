import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def subscribers(): click.echo('ConvertKit subscribers')
@cli.command()
def forms(): click.echo('ConvertKit forms')
if __name__ == '__main__': cli()
